package ugm.dteti.se.eplat.model;

import com.google.gson.annotations.SerializedName;

/**
 * Created by eplat on 31/08/17.
 */

public class EplatData {

    public EplatData(String deviceId, String lat, String lon, String direction) {
        this.deviceId = deviceId;
        this.lat = lat;
        this.lon = lon;
        this.direction = direction;
    }

    @SerializedName("device_id")
    private String deviceId;
    @SerializedName("lat")
    private String lat;
    @SerializedName("lon")
    private String lon;
    @SerializedName("direction")
    private String direction;

    public String getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(String deviceId) {
        this.deviceId = deviceId;
    }

    public String getLat() {
        return lat;
    }

    public void setLat(String lat) {
        this.lat = lat;
    }

    public String getLon() {
        return lon;
    }

    public void setLon(String lon) {
        this.lon = lon;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
}
