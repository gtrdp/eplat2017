package ugm.dteti.se.eplat.rest;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;
import ugm.dteti.se.eplat.model.SnapToRoadResult;

/**
 * Created by gtrdp on 03/09/2017.
 */

public interface SnapToRoadInterface {
    @GET("v1/snapToRoads")
    Call<SnapToRoadResult> getSnapToRoad(@Query("interpolate") String interpolate,
                                         @Query("path") String path, @Query("key") String apiKey);
}
