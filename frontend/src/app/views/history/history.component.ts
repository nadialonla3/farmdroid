import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  add(newNumb: number=0,newDate: string = "newDate", newCollectorName:string = "NewNodeName", newActionName:string="newAction"){
    var lines = document.getElementById("tableBodyHistory");
    var str = `<tr>
    <th scope="row">${newNumb}</th>
    <td>${newDate}</td>
    <td>${newCollectorName}</td>
    <td>${newActionName}</td>
  </tr>`+lines.innerHTML;
    lines.innerHTML = str;
  }
}
