package ugm.dteti.se.eplat.activity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import ugm.dteti.se.eplat.R;
import ugm.dteti.se.eplat.model.EplatData;
import ugm.dteti.se.eplat.model.SnappedPoint;
import ugm.dteti.se.eplat.rest.ApiClient;
import ugm.dteti.se.eplat.rest.ApiInterface;

public class MainActivity extends AppCompatActivity{

    EditText editAdress;
    EditText editDeviceId;
    EditText editDelay;

    String deviceId, lat, lon, serverAddress;
    private int delay;
    static final int PICK_LOCATION_REQUEST = 1;  // The request code

    ApiInterface apiService;
    private static final String TAG = MainActivity.class.getSimpleName();
    public static final String BASE_URL = "http://10.42.10.211:5000/"; // for raspi

    private List<SnappedPoint> snappedPoints = new ArrayList<>();
    ProgressDialog dlg = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editAdress = (EditText) findViewById(R.id.edtServerAddress);
        editDeviceId = (EditText) findViewById(R.id.edtDeviceId);
        editDelay = (EditText) findViewById(R.id.edtTimeInterval);

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
                if (!snappedPoints.isEmpty()) {
                    // start the api service
                    serverAddress = "http://" + editAdress.getText().toString() + ":5000/";
                    apiService = ApiClient.getClient(serverAddress).create(ApiInterface.class);

                    // prepare the data
                    deviceId = editDeviceId.getText().toString();
                    delay = Integer.valueOf(editDelay.getText().toString());

                    // prepare the loading dialog
                    dlg = new ProgressDialog(MainActivity.this);
                    dlg.setMessage("Sending data...");
                    dlg.setCancelable(true);
                    dlg.show();

                    // start the loop
                    sendLoop();
                } else {
                    Toast.makeText(getApplicationContext(),
                            "Please select direction first!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void sendLoop() {
        final Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                sendData();
            }
        }, delay);
    }

    private void sendData() {
        if (!snappedPoints.isEmpty()) {
            // prepare data
            SnappedPoint sp = snappedPoints.get(0);
            snappedPoints.remove(0);
            Log.d("Snapped Ppoints size", Integer.toString(snappedPoints.size()));

            Call<ResponseBody> call = apiService.sendEplatData(new EplatData(deviceId,
                    sp.getLoc().getLatitude(), sp.getLoc().getLongitude(), "north"));

            call.enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                    Log.d(TAG, Integer.toString(response.code()));
                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable t) {
                    Log.e(TAG, t.toString());
                }
            });

            sendLoop();
        } else {
            // send exit message
//            Call<ResponseBody> call = apiService.sendEplatData(new EplatData(deviceId,
//                    0d, 0d, "north"));
//
//            call.enqueue(new Callback<ResponseBody>() {
//                @Override
//                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
//                    Log.d(TAG, Integer.toString(response.code()));
//                }
//
//                @Override
//                public void onFailure(Call<ResponseBody> call, Throwable t) {
//                    Log.e(TAG, t.toString());
//                }
//            });

            dlg.dismiss();
            Toast.makeText(getApplicationContext(), "Done!", Toast.LENGTH_SHORT).show();
        }
    }

    // get the returned path from google maps

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_LOCATION_REQUEST) {
            if (resultCode == RESULT_OK) {
                String sp = data.getStringExtra("snappedPoints");

                // convert json to pojo
                Gson gson = new Gson();
                Type type = new TypeToken<List<SnappedPoint>>() {}.getType();
                snappedPoints = gson.fromJson(sp, type);
            }
        }
    }
}
