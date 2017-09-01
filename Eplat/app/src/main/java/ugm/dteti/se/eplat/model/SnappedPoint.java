package ugm.dteti.se.eplat.model;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by gtrdp on 01/09/2017.
 */

public class SnappedPoint {
    @SerializedName("location")
    private Location loc;
    @SerializedName("originalIndex")
    private int originalIndex;
    @SerializedName("placeId")
    private String placeId;

    public Location getLoc() {
        return loc;
    }

    public void setLoc(Location loc) {
        this.loc = loc;
    }

    public int getOriginalIndex() {
        return originalIndex;
    }

    public void setOriginalIndex(int originalIndex) {
        this.originalIndex = originalIndex;
    }

    public String getPlaceId() {
        return placeId;
    }

    public void setPlaceId(String placeId) {
        this.placeId = placeId;
    }
}
