package ugm.dteti.se.eplat.model;

import com.google.gson.annotations.SerializedName;

/**
 * Created by gtrdp on 01/09/2017.
 */

public class Location {
    @SerializedName("latitude")
    private Double latitude;
    @SerializedName("longitude")
    private Double longitude;

    public Double getLatitude() {
        return latitude;
    }

    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public Double getLongitude() {
        return longitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }
}
