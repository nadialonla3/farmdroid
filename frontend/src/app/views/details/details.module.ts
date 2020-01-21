import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DetailsComponent } from './details/details.component';
import { AppSidebarModule } from '@coreui/angular';
import { PerfectScrollbarModule } from 'ngx-perfect-scrollbar';
import { DetailsRoutingModule } from './details-routing.module';
import { LineChartComponent } from '../line-chart-component/line-chart-component.component';
import { ChartsModule } from 'ng2-charts';

@NgModule({
  declarations: [DetailsComponent,
    LineChartComponent,],
  imports: [
    CommonModule,
    AppSidebarModule,
    PerfectScrollbarModule,
    ChartsModule,
    DetailsRoutingModule
  ]
})
export class DetailsModule { }
