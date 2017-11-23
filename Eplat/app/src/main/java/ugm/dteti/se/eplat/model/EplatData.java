package ugm.dteti.se.eplat.model;

import com.google.gson.annotations.SerializedName;

/**
 * Created by eplat on 31/08/17.
 */

public class EplatData {

    public EplatData(String deviceId, Integer vType, Double lat, Double lon, String direction) {
        this.deviceId = deviceId;
        this.lat = lat;
        this.lon = lon;
        this.direction = direction;
        this.vehicleType = vType;
    }

    @SerializedName("device_id")
    private String deviceId;
    @SerializedName("vehicle_type")
    private Integer vehicleType;
    @SerializedName("lat")
    private Double lat;
    @SerializedName("lon")
    private Double lon;
    @SerializedName("direction")
    private String direction;

    public String getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(String deviceId) {
        this.deviceId = deviceId;
    }

    public Double getLat() {
        return lat;
    }

    public void setLat(Double lat) {
        this.lat = lat;
    }

    public Double getLon() {
        return lon;
    }

    public void setLon(Double lon) {
        this.lon = lon;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public Integer getVehicleType() {
        return vehicleType;
    }

    public void setVehicleType(Integer vehicleType) {
        this.vehicleType = vehicleType;
    }
}
