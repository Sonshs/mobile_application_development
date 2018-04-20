package qqq.example.com.ex2;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class MainActivity extends AppCompatActivity {
    private double u2v = 22774.93;
    private double v2u = 0.0000439079;
    private double g2v = 32019.81;
    private double v2g = 0.0000312307;
    private double g2u = 1.40589;
    private double u2g = 0.711293;
    private String ann = "Wrong input!";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button btn = (Button) findViewById(R.id.button);
        btn.setOnClickListener(new View.OnClickListener(){                          // listerner for button
            @Override
            public void onClick(View v){
                Spinner mySpinner=(Spinner) findViewById(R.id.spinner1);
                String text = mySpinner.getSelectedItem().toString();               // get content of spinner
                EditText edt_cur1 = (EditText) findViewById(R.id.edt_cur1);         // get value of currency need to convert
                String str_cur1 = edt_cur1.getText().toString();
                TextView tv1 = (TextView) findViewById(R.id.tv_cur2_val);           // result/announce after convert
                double dbl_cur1 = 0;
                double cur2;
                boolean canpar;
             // check that value can parse to Double?
                try {
                    dbl_cur1 = Double.parseDouble(str_cur1);
                    canpar = true;
                }
                catch (Exception e){
                    canpar = false;
                }

            // if can parse, start convert. Else print announcement
                if (canpar){
                    if (text.equals("USD to VND")){
                        cur2 = dbl_cur1*u2v;
                    }
                    else if (text.equals("VND to USD")) {
                        cur2 = dbl_cur1*v2u;
                    }
                    else if (text.equals("VND to GBP")) {
                        cur2 = dbl_cur1*v2g;
                    }
                    else if (text.equals("GBP to USD")) {
                        cur2 = dbl_cur1*g2u;
                    }
                    else if (text.equals("GBP to VND")) {
                        cur2 = dbl_cur1*g2v;
                    }
                    else
                        cur2 = dbl_cur1*u2g;
                    cur2 = BigDecimal.valueOf(cur2)
                            .setScale(4, RoundingMode.HALF_UP)
                            .doubleValue();

                    tv1.setText(String.valueOf(cur2));
                }
                else{
                    tv1.setText(ann);
                }
            }
        });
    }
}


