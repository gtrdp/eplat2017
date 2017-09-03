package ugm.dteti.se.eplat.rest;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query;
import ugm.dteti.se.eplat.model.EplatData;
import ugm.dteti.se.eplat.model.SnapToRoadResult;;

/**
 * Created by eplat on 31/08/17.
 */

public interface ApiInterface {
    @POST("api")
    Call<ResponseBody> sendEplatData(@Body EplatData data);
}
