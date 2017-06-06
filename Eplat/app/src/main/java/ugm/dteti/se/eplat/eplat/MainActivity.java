package ugm.dteti.se.eplat.eplat;

import android.content.Context;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.gson.GsonBuilder;

import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btnStart = (Button) findViewById(R.id.btnStart);
        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "Sending the data!", Toast.LENGTH_SHORT).show();

                new PostJSON("http://10.42.10.248:5000").execute();
            }
        });
    }
}

class PostJSON extends AsyncTask<String, Void, String> {

    private String uri;

    public PostJSON(String u) {
        uri = u;
    }

    @Override
    protected String doInBackground(String... arg0) {
        // TODO Auto-generated method stub
        return execute();
    }

    private String execute() {
        // creates a JSON object with the below
        Map<String, String> vehicle = new HashMap<>();
        vehicle.put("id", "12345");
        vehicle.put("lat", "-7.797068");
        vehicle.put("long", "110.370529");
        vehicle.put("dir", "S");

        String json = new GsonBuilder().create().toJson(vehicle, Map.class);

        Log.v("JSON Result", json);
        return makeRequest(uri, json).toString();
    }

    public String makeRequest(String uri, String json) {
        HttpClient httpclient = new DefaultHttpClient();
        HttpPost httpPost = new HttpPost(uri);
        try {
            //HttpPost httpPost = new HttpPost(uri);
            httpPost.setEntity(new StringEntity(json));
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");
            System.out.println("Call successful");
            //return new DefaultHttpClient().execute(httpPost);
            // Execute HTTP Post Request
            ResponseHandler<String> responseHandler=new BasicResponseHandler();
            return httpclient.execute(httpPost, responseHandler);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    protected void onPostExecute(String result) {
        //Call the intent and pass the id from the http post response
        System.out.println("Result: " + result);
    }
}
