import { Component, OnInit, ViewChild, TrackByFunction, Input } from '@angular/core';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { Color, BaseChartDirective, Label } from 'ng2-charts';
//import * as pluginAnnotations from 'chartjs-plugin-annotation';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart-component.component.html',
  styleUrls: ['./line-chart-component.component.css']
})
export class LineChartComponent implements OnInit {
  @Input() tabX: string[];
  @Input() tabY: number[];
  @Input() graphTitle:string;
  @Input() colors: Color[];

  public lineChartData: ChartDataSets[];
  public lineChartLabels: Label[];
  public lineChartOptions: (ChartOptions & { annotation: any });
  public lineChartColors: Color[];
  public lineChartLegend;
  public lineChartType;
  public lineChartPlugins;

  constructor() {
    
   }

  ngOnInit() {
    this.lineChartData = [
      { data: this.tabY, label: this.graphTitle },
    ];
    this.lineChartLabels = this.tabX;
    this.lineChartOptions = {
      responsive: true,
      scales: {
        // We use this empty structure as a placeholder for dynamic theming.
        xAxes: [{}],
        yAxes: [
          {
            id: 'y-axis-0',
            position: 'left',
          },
        ]
      },
      annotation: {
        annotations: [
          {
            type: 'line',
            mode: 'vertical',
            scaleID: 'x-axis-0',
            value: 'March',
            borderColor: 'orange',
            borderWidth: 2,
            label: {
              enabled: true,
              fontColor: 'orange',
              content: 'LineAnno'
            }
          },
        ],
      },
    };
    // this.colors =  [
    //   {
    //     borderColor: 'black',
    //     backgroundColor: 'rgba(255,0,0,0.3)',
    //   },
    // ];
    this.lineChartColors = this.colors
    this.lineChartLegend  = true;
    this.lineChartType = 'line';
    this.lineChartPlugins = [];
  }
}