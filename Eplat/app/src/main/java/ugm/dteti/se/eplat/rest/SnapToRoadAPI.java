package ugm.dteti.se.eplat.rest;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * Created by gtrdp on 03/09/2017.
 */

public class SnapToRoadAPI {
    public static final String BASE_URL = "https://roads.googleapis.com/"; // for GMaps snap to road
    private static Retrofit retrofit = null;


    public static Retrofit getClient() {
        if (retrofit==null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit;
    }
}
