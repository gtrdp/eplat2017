package ugm.dteti.se.eplat.model;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by gtrdp on 01/09/2017.
 */

public class SnapToRoadResult {
    @SerializedName("snappedPoints")
    private List<SnappedPoint> snappedPoints;

    public List<SnappedPoint> getSnappedPoints() {
        return snappedPoints;
    }

    public void setSnappedPoints(List<SnappedPoint> snappedPoints) {
        this.snappedPoints = snappedPoints;
    }
}
