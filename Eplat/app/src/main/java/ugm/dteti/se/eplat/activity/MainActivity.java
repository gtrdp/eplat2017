package ugm.dteti.se.eplat.activity;

import android.content.Intent;
import android.support.annotation.IntegerRes;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import ugm.dteti.se.eplat.R;
import ugm.dteti.se.eplat.model.EplatData;
import ugm.dteti.se.eplat.model.SnappedPoint;
import ugm.dteti.se.eplat.rest.ApiClient;
import ugm.dteti.se.eplat.rest.ApiInterface;

public class MainActivity extends AppCompatActivity{

    EditText editAdress;
    EditText editDeviceId;

    String deviceId, lat, lon, serverAddress;
    static final int PICK_LOCATION_REQUEST = 1;  // The request code

    ApiInterface apiService;
    private static final String TAG = MainActivity.class.getSimpleName();
    public static final String BASE_URL = "http://10.42.10.211:5000/"; // for raspi

    private List<SnappedPoint> snappedPoints = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editAdress = (EditText) findViewById(R.id.edtServerAddress);
        editDeviceId = (EditText) findViewById(R.id.edtDeviceId);

        // Button Map
        Button btnMap = (Button) findViewById(R.id.btnMap);
        btnMap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivityForResult(new Intent(MainActivity.this, MapActivity.class), PICK_LOCATION_REQUEST);
            }
        });

        deviceId = editDeviceId.getText().toString();
        serverAddress = "http://" + editAdress.getText().toString() + ":5000";
        lat = "-7.797068";
        lon = "110.370529";

        Button btnStart = (Button) findViewById(R.id.btnStart);
        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (snappedPoints != null) {
                    Toast.makeText(getApplicationContext(),
                            "Sending the data!", Toast.LENGTH_SHORT).show();
                    // start the api service
                    apiService = ApiClient.getClient(BASE_URL).create(ApiInterface.class);

                    // prepare the data
                    EplatData data = getParameters();

                    // execute
                    Call<ResponseBody> call = apiService.sendEplatData(data);
                    call.enqueue(new Callback<ResponseBody>() {
                        @Override
                        public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                            Log.d(TAG, response.body().toString());
                        }

                        @Override
                        public void onFailure(Call<ResponseBody> call, Throwable t) {
                            Log.e(TAG, t.toString());
                        }
                    });
                } else {
                    Toast.makeText(getApplicationContext(),
                            "Please select direction first!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    public EplatData getParameters() {
        deviceId = editDeviceId.getText().toString();
        serverAddress = "http://" + editAdress.getText().toString() + ":5000";
        lat = "-7.797068";
        lon = "110.370529";

        return new EplatData(deviceId, lat, lon, "");
    }

    // get the returned path from google maps

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_LOCATION_REQUEST) {
            if (resultCode == RESULT_OK) {
                String snappedPoints = data.getStringExtra("snappedPoints");

                Log.d("Result Snapped Points", snappedPoints);
            }
        }
    }
}