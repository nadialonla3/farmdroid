import { Component, OnInit } from '@angular/core';
import { nodeItems } from './_navNode';
import { LineChartComponent } from '../../line-chart-component/line-chart-component.component';
import { Color, BaseChartDirective, Label } from 'ng2-charts';


@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {

  public color1 : Color[];
  public color2 : Color[];
  public color3 : Color[];
  public color4 : Color[];
  public color5 : Color[];
  public color6 : Color[];
  public color7 : Color[];
  public color8 : Color[];

  public graph1 : string;
  public graph2 : string;
  public graph3 : string;
  public graph4 : string;
  public graph5 : string;
  public graph6 : string;
  public graph7 : string;
  public graph8 : string;

  public tabX1 : string [];
  public tabX2 : string [];
  public tabX3 : string [];
  public tabX4 : string [];
  public tabX5 : string [];
  public tabX6 : string [];
  public tabX7 : string [];
  public tabX8 : string [];

  public tabY1 : number [];
  public tabY2 : number [];
  public tabY3 : number [];
  public tabY4 : number [];
  public tabY5 : number [];
  public tabY6 : number [];
  public tabY7 : number [];
  public tabY8 : number [];

  constructor() { }

  ngOnInit() {
    this.color1 =  [
      {
        borderColor: 'rgba(255,0,0,0.3)',
        backgroundColor: 'rgba(255,0,0,0.3)',
      },
    ];
    this.color2 =  [
      {
        borderColor: 'rgba(45, 62, 211, 0.6)',
        backgroundColor: 'rgba(45, 62, 211, 0.6)',
      },
    ];
    this.color3 =  [
      {
        borderColor: 'dark-gray',
        backgroundColor: 'dark-gray',
      },
    ];
    this.color4 =  [
      {
        borderColor: 'rgb(255,200,0,0.3)',
        backgroundColor: 'rgb(255,200,0,0.3)',
      },
    ];
    this.color5 =  [
      {
        borderColor: 'rgb(25,0,0,0.3)',
        backgroundColor: 'rgb(25,0,0,0.3)',
      },
    ];
    this.color6 =  [
      {
        borderColor: 'rgb(0,240,0,0.3)',
        backgroundColor: 'rgb(0,240,0,0.3)',
      },
    ];
    this.color7 =  [
      {
        borderColor: 'rgb(255,50,0,0.3)',
        backgroundColor: 'rgb(255,50,0,0.3)',
      },
    ];
    this.color8 =  [
      {
        borderColor: 'rgb(255,120,0,0.3)',
        backgroundColor: 'rgb(255,120,0,0.3)',
      },
    ];

    this.graph1 = 'graph of soil temperature sensors';
    this.graph2 = 'graph of soil pressure sensors';
    this.graph3 = 'graph of ph sensors';
    this.graph4 = 'sensors of CO2 graph';
    this.graph5 = 'graph of air temperature sensors';
    this.graph6 = 'graph of air humidity sensors';
    this.graph7 = 'luminosity sensors graph';
    this.graph8 = 'graph of Pressure sensors';

    this.tabX1 = ['0','5','10','15','20','22','24H'];
    this.tabX2 = ['0','5','10','15','20','22','24H'];
    this.tabX3 = ['0','5','10','15','20','22','24H'];
    this.tabX4 = ['0','5','10','15','20','22','24H'];
    this.tabX5 = ['0','5','10','15','20','22','24H'];
    this.tabX6 = ['0','5','10','15','20','22','24H'];
    this.tabX7 = ['0','5','10','15','20','22','24H'];
    this.tabX8 = ['0','5','10','15','20','22','24H'];

    this.tabY1 = [35,10,5,7,13,6,6];
    this.tabY2 = [35,10,5,7,13,6,6];
    this.tabY3 = [35,10,5,7,13,6,6];
    this.tabY4 = [35,10,5,7,13,6,6];
    this.tabY5 = [35,10,5,7,13,6,6];
    this.tabY6 = [35,10,5,7,13,6,6];
    this.tabY7 = [35,10,5,7,13,6,6];
    this.tabY8 = [35,10,5,7,13,6,6];

    
  }

  public changer() {
    console.log('je suis entré dans la fonction changer');
    this.tabY1 = [100,100,100,100,100,100,100];
    console.log(this.tabY1);
  }

  public sidebarMinimized = false;
  public navItems = nodeItems;

  toggleMinimize(e) {
    this.sidebarMinimized = e;
  }

  chart1: LineChartComponent;
  numero_noeud_ordinaire = 1;
  

  
}
