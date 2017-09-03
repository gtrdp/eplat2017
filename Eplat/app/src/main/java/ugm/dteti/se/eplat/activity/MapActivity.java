package ugm.dteti.se.eplat.activity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.PolylineOptions;
import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import ugm.dteti.se.eplat.R;
import ugm.dteti.se.eplat.model.SnapToRoadResult;
import ugm.dteti.se.eplat.model.SnappedPoint;
import ugm.dteti.se.eplat.rest.ApiClient;
import ugm.dteti.se.eplat.rest.ApiInterface;
import ugm.dteti.se.eplat.rest.SnapToRoadAPI;
import ugm.dteti.se.eplat.rest.SnapToRoadInterface;

public class MapActivity extends AppCompatActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private String[] markerLabels = {"Start", "Crossing", "Stop"};
    private List<Marker> markers = new ArrayList<Marker>();

    public static final String BASE_URL = "https://roads.googleapis.com/"; // for GMaps snap to road
    private final static String API_KEY = "AIzaSyC-xk4f97rKVqJg3YWVccEx83uguofc97o";

    private SnapToRoadInterface strInterface;

    private List<SnappedPoint> snappedPoints = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // Get the SupportMapFragment and request notification
        // when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        // btn reset map
        Button btnResetMarker = (Button) findViewById(R.id.btnResetMarker);
        btnResetMarker.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getApplicationContext(), "Marker is reset.", Toast.LENGTH_SHORT).show();
                mMap.clear();
                markers.clear();
            }
        });

        // btn confirm
        Button btnConfirm = (Button) findViewById(R.id.btnConfirmMarker);
        btnConfirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (markers.size() == 3) {
                    Toast.makeText(getApplicationContext(), "OK Ready to go.", Toast.LENGTH_SHORT).show();

                    // set the returned data
                    Gson gson = new Gson();
                    Intent data = new Intent();
                    data.putExtra("snappedPoints", gson.toJson(snappedPoints));
                    setResult(RESULT_OK, data);

                    finish();
                } else {
                    Toast.makeText(getApplicationContext(),
                            "Please set starting, crossing, and ending markers.",
                            Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Google Maps snap to road API
        strInterface = SnapToRoadAPI.getClient().create(SnapToRoadInterface.class);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        LatLng crossRoad = new LatLng(-7.762007, 110.369383);
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(crossRoad));
        googleMap.moveCamera(CameraUpdateFactory.zoomTo(17.0f));

        // add marker on click
        googleMap.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {
                if (markers.size() < 3) {
                    LatLng crossRoad = new LatLng(latLng.latitude, latLng.longitude);
                    Marker locationMarker = mMap.addMarker(new MarkerOptions().position(crossRoad)
                            .title(markerLabels[markers.size()]));
                    locationMarker.showInfoWindow();

                    markers.add(locationMarker);
                    Log.i("Marker", Integer.toString(markers.size()));

                    if (markers.size() == 3) {
                        // get the marker coordinates
                        String path = "";
                        for (int i = 0; i < markers.size(); i++) {
                            Marker m = markers.get(i);
                            String lat = Double.toString(m.getPosition().latitude);
                            String lon = Double.toString(m.getPosition().longitude);

                            path += lat + "," + lon + "|";
                        }
                        path = path.substring(0, path.length() - 1); // remove trailing pipe |

                        Call<SnapToRoadResult> call = strInterface.getSnapToRoad("true",
                                path, API_KEY);
                        call.enqueue(new Callback<SnapToRoadResult>() {
                            @Override
                            public void onResponse(Call<SnapToRoadResult> call, Response<SnapToRoadResult> response) {
                                Log.d("JSON Result", response.message());

                                snappedPoints = response.body().getSnappedPoints();
                                drawPath(snappedPoints);
                            }

                            @Override
                            public void onFailure(Call<SnapToRoadResult> call, Throwable t) {
                                Toast.makeText(getApplicationContext(), "An error occured" + t.toString(),
                                        Toast.LENGTH_LONG).show();
                                Log.e("Error Response", t.toString());
                            }
                        });
                    }
                }
            }
        });
    }

    private void drawPath(List<SnappedPoint> snappedPoints) {
        PolylineOptions options = new PolylineOptions().width(7).color(Color.BLUE).geodesic(true);

        for (int i = 0; i < snappedPoints.size(); i++) {
            SnappedPoint sp = snappedPoints.get(i);
            LatLng point = new LatLng(sp.getLoc().getLatitude(), sp.getLoc().getLongitude());
            options.add(point);
        }

        mMap.addPolyline(options);
    }
}
