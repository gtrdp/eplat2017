package ugm.dteti.se.eplat.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;

import ugm.dteti.se.eplat.R;

public class LauncherActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_launcher);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // simulation button
        Button simulationButton = (Button) findViewById(R.id.btnSimulate);
        simulationButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(LauncherActivity.this, MainActivity.class);
                startActivity(i);
            }
        });

        // eplat client button
        Button clientButton = (Button) findViewById(R.id.btnEplatClient);
        clientButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(LauncherActivity.this, EPlatClient.class);
                startActivity(i);
            }
        });

        // eplat manual simulation button
        Button manualSimulationButton = (Button) findViewById(R.id.btnManualSimulate);
        manualSimulationButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(LauncherActivity.this, ManualSimulation.class);
                startActivity(i);
            }
        });

//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });
    }

}
