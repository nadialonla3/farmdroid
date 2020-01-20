import { Injectable , OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PhService implements OnInit{

  value 
  values : string[];

  constructor(private http : HttpClient) { }

  ngOnInit(): void {
    this.ActualValue();
    console.log("je suis dans le ngoninit")
  }

  ActualValue() {

  const url = "http://localhost:8000/cultures/data1/5";
  let req = new Request( url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'mode': 'no-cors',
      'Access-Control-Allow-Origin': '*',
    }
  });

  fetch(req)
    .then(response => this.values= response['results'][1])
    // {}response.text()
    .then((contents) => {
      this.value = JSON.parse(contents);
      console.log(JSON.parse(contents).data)
      if (this.value.data) {
       // do something
      } else {
       // do something
      }
    })
    .catch(() => console.log("Can’t access " + url + " response. Blocked by browser?"))

    // this.http.get("http://localhost:8000/cultures/data1/5")
    // .subscribe((response)=>{
    //   this.values = response['results'][1];
    // }, (err)=>{
    //   console.log(err);
    // })
  }

  AllValue(firstDate : Date, lastDate : Date ) {
    this.http.get("http://localhost:8000/cultures/data/ph"+firstDate.toString()+'/'+lastDate.toString())
    .subscribe((response)=>{
      this.values = response['results'];
    }, (err)=>{
      console.log(err);
    })
  }

  ActualMeanValue() {
    this.http.get("http://localhost:8000/cultures/dataMean/ph")
    .subscribe((response)=>{
      this.value = response['results'][0];
    }, (err)=>{
      console.log(err);
    })
  }

  AllMeanValue(firstDate : Date, lastDate : Date ) {
    this.http.get("http://localhost:8000/cultures/dataMean/ph"+firstDate.toString()+'/'+lastDate.toString())
    .subscribe((response)=>{
      this.values = response['results'];
    }, (err)=>{
      console.log(err);
    })
  }
}
