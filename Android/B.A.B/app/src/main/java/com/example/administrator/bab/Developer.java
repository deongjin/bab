package com.example.administrator.bab;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;

import static com.example.administrator.bab.Mainactivity.logo_num;

public class Developer extends AppCompatActivity {

    LinearLayout Activity_developer, Logo;
    ImageView Bab;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_developer);

        Bab = (ImageView)findViewById(R.id.bab);
        Logo = (LinearLayout)findViewById(R.id.logo);

        Activity_developer = (LinearLayout)findViewById(R.id.activity_developer);

        Activity_developer.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                finish();
            }
        });

        Logo.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                change_logo();
            }
        });

        switch(logo_num % 9){                                           //로고 초기 색상 설정
            case 0 : Bab.setImageResource(R.drawable.bablogo_white) ;break;
            case 1 : Bab.setImageResource(R.drawable.red) ;break;
            case 2 : Bab.setImageResource(R.drawable.orange) ;break;
            case 3 : Bab.setImageResource(R.drawable.yellow) ;break;
            case 4 : Bab.setImageResource(R.drawable.green) ;break;
            case 5 : Bab.setImageResource(R.drawable.skyblue) ;break;
            case 6 : Bab.setImageResource(R.drawable.navy) ;break;
            case 7 : Bab.setImageResource(R.drawable.violet) ;break;
            case 8 : Bab.setImageResource(R.drawable.bablogo_white_knife); break;
            default:break;
        }
    }

    public void change_logo(){
        logo_num++;
        switch(logo_num % 9){
            case 0 : Bab.setImageResource(R.drawable.bablogo_white) ;break;
            case 1 : Bab.setImageResource(R.drawable.red) ;break;
            case 2 : Bab.setImageResource(R.drawable.orange) ;break;
            case 3 : Bab.setImageResource(R.drawable.yellow) ;break;
            case 4 : Bab.setImageResource(R.drawable.green) ;break;
            case 5 : Bab.setImageResource(R.drawable.skyblue) ;break;
            case 6 : Bab.setImageResource(R.drawable.navy) ;break;
            case 7 : Bab.setImageResource(R.drawable.violet) ;break;
            case 8 : Bab.setImageResource(R.drawable.bablogo_white_knife); break;
            default:break;
        }
    }                 //로고 이미지 변화 함수
}
