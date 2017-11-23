package ugm.dteti.se.eplat.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import ugm.dteti.se.eplat.R;

import static ugm.dteti.se.eplat.activity.MainActivity.PICK_LOCATION_REQUEST;

public class ManualSimulation extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    private EditText editAdress, editDeviceId;
    private Spinner spinnerVehicleType;
    private String deviceId, serverAddress, lat, lon;
    private Integer vehicleType;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_manual_simulation);

        editAdress = (EditText) findViewById(R.id.editServerAddress);
        editDeviceId = (EditText) findViewById(R.id.editDevID);

        deviceId = editDeviceId.getText().toString();
        serverAddress = "http://" + editAdress.getText().toString() + ":5000";
        lat = "-7.797068";
        lon = "110.370529";

        spinnerVehicleType = (Spinner) findViewById(R.id.spinVehicleId);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.vehicle_type, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerVehicleType.setAdapter(adapter);
        spinnerVehicleType.setOnItemSelectedListener(this);

        // Button Map
        Button btnMap = (Button) findViewById(R.id.btnManualMap);
        btnMap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ManualSimulation.this, ManualMapActivity.class);
                i.putExtra("vehicleID", deviceId);
                i.putExtra("vehicleType", vehicleType);
                i.putExtra("serverAddress", serverAddress);

                startActivity(i);
            }
        });
    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        Log.d("item click", Integer.toString(i));
        vehicleType = i;
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }
}
