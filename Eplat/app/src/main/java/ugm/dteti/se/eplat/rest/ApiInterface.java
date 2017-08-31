package ugm.dteti.se.eplat.rest;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;
import ugm.dteti.se.eplat.model.EplatData;

/**
 * Created by eplat on 31/08/17.
 */

public interface ApiInterface {
    @POST("api")
    Call<ResponseBody> sendEplatData(@Body EplatData data);
}
