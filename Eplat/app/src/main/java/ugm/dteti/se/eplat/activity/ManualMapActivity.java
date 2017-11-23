package ugm.dteti.se.eplat.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptor;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import ugm.dteti.se.eplat.R;
import ugm.dteti.se.eplat.model.EplatData;
import ugm.dteti.se.eplat.model.SnapToRoadResult;
import ugm.dteti.se.eplat.rest.ApiClient;
import ugm.dteti.se.eplat.rest.ApiInterface;

public class ManualMapActivity extends AppCompatActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private Marker trafficLightMarker, vehicleMarker = null;
    String vehicleID, serverAddress;
    Integer vehicleType;
    BitmapDescriptor icon;
    ApiInterface apiService;

    private static final String TAG = MainActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_manual_map);

        // get extras
        Intent i = getIntent();
        vehicleID = i.getStringExtra("vehicleID");
        vehicleType = i.getIntExtra("vehicleType", 0);
        serverAddress = i.getStringExtra("serverAddress");

        apiService = ApiClient.getClient(serverAddress).create(ApiInterface.class);

        // Get the SupportMapFragment and request notification
        // when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.manualMap);
        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        LatLng crossRoad = new LatLng(-7.762007, 110.369383);
        mMap.moveCamera(CameraUpdateFactory.newLatLng(crossRoad));
        mMap.moveCamera(CameraUpdateFactory.zoomTo(17.0f));
        mMap.getUiSettings().setAllGesturesEnabled(false);

//        // add traffic light marker
//        icon = BitmapDescriptorFactory.fromResource(R.drawable.traffic);
//        trafficLightMarker = mMap.addMarker(new MarkerOptions().position(new LatLng(-7.762049, 110.369364))
//                .title("Traffic Light").icon(icon));

        // add marker on click
        mMap.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {
                Log.d("Map coordinate", Double.toString(latLng.latitude) + ", " + Double.toString(latLng.longitude));

                LatLng latlon = new LatLng(latLng.latitude, latLng.longitude);

                if (vehicleMarker == null) {
                    // add new marker
                    vehicleMarker = mMap.addMarker(new MarkerOptions().position(latlon));
                } else {
                    // update existing marker
                    vehicleMarker.setPosition(latlon);
                }

                // send data to server
                Call<ResponseBody> call = apiService.sendEplatData(new EplatData(vehicleID, vehicleType,
                        latLng.latitude, latLng.longitude, "north"));

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
            }
        });

        mMap.setOnMapLongClickListener(new GoogleMap.OnMapLongClickListener() {
            @Override
            public void onMapLongClick(LatLng latLng) {
                Log.d("Map coordinate long", Double.toString(latLng.latitude) + ", " + Double.toString(latLng.longitude));
            }
        });
    }

    @Override
    protected void onStop() {
        super.onStop();

        // send exit message
        Log.d(TAG, "Sending exit message.");
        Call<ResponseBody> call = apiService.sendEplatData(new EplatData(vehicleID, vehicleType,
                0d, 0d, "north"));

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

        Toast.makeText(getApplicationContext(), "Done!", Toast.LENGTH_SHORT).show();
    }
}
