import { Component, OnInit, ViewChild, TrackByFunction } from '@angular/core';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { Color, BaseChartDirective, Label } from 'ng2-charts';
//import * as pluginAnnotations from 'chartjs-plugin-annotation';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  constructor(public tabX : string[], public tabY : number[], public lineChartColors: Color[], 
    public lineChartLegend : boolean, public lineChartType : string,
    public lineChartLabels : Label[], public lineChartData: ChartDataSets[],
    public lineChartOptions: (ChartOptions & { annotation: any })) {
    
  }

  // tabX: string[] = ['-5','-3','-0,5','0','1','2','9'];
  // tabY: number[] = [4,10,-2,7,-20,6,6];

  // public lineChartData: ChartDataSets[] = [
  //   { data: this.tabY, label: 'Nom de la Courbe' },
  // ];

  // public lineChartLabels: Label[] = this.tabX;

  // public lineChartOptions: (ChartOptions & { annotation: any }) = {
  //   responsive: true,
  //   scales: {
  //     // We use this empty structure as a placeholder for dynamic theming.
  //     xAxes: [{}],
  //     yAxes: [
  //       {
  //         id: 'y-axis-0',
  //         position: 'left',
  //       },
  //     ]
  //   },
  //   annotation: {
  //     annotations: [
  //       {
  //         type: 'line',
  //         mode: 'vertical',
  //         scaleID: 'x-axis-0',
  //         value: 'March',
  //         borderColor: 'orange',
  //         borderWidth: 2,
  //         label: {
  //           enabled: true,
  //           fontColor: 'orange',
  //           content: 'LineAnno'
  //         }
  //       },
  //     ],
  //   },
  // };
  // public lineChartColors: Color[] = [
  //   {
  //     borderColor: 'black',
  //     backgroundColor: 'rgba(255,0,0,0.3)',
  //   },
  // ];
  // public lineChartLegend = true;
  // public lineChartType = 'line';
   public lineChartPlugins = [];

  ngOnInit() {
  }
}