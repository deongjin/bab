package com.example.administrator.bab;


import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class Loading extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);
        startLoading();
    }
    private void startLoading(){                            // 2초 지연 후 끝내는 함수
        Handler handler = new Handler();
        handler.postDelayed(new Runnable(){
            @Override
            public void run(){
                finish();
            }
        }, 2000);
    }
}
