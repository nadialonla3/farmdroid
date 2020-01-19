import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SoilHumidityService {

  value : number;
  values : number[];

  constructor(private http : HttpClient) { }

  ActualValue() {
    this.http.get("http://localhost:8000/cultures/data/soilHumidity")
    .subscribe((response)=>{
      this.value = response['results'][0];
    }, (err)=>{
      console.log(err);
    })
  }

  AllValue(firstDate : Date, lastDate : Date ) {
    this.http.get("http://localhost:8000/cultures/data/soilHumidity"+firstDate.toString()+'/'+lastDate.toString())
    .subscribe((response)=>{
      this.values = response['results'];
    }, (err)=>{
      console.log(err);
    })
  }

  ActualMeanValue() {
    this.http.get("http://localhost:8000/cultures/dataMean/soilHumidity")
    .subscribe((response)=>{
      this.value = response['results'][0];
    }, (err)=>{
      console.log(err);
    })
  }

  AllMeanValue(firstDate : Date, lastDate : Date ) {
    this.http.get("http://localhost:8000/cultures/dataMean/soilHumidity"+firstDate.toString()+'/'+lastDate.toString())
    .subscribe((response)=>{
      this.values = response['results'];
    }, (err)=>{
      console.log(err);
    })
  }
}
