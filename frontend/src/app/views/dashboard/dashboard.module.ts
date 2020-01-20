import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChartsModule } from 'ng2-charts';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { ButtonsModule } from 'ngx-bootstrap/buttons';

import { DashboardComponent } from './dashboard.component';
import { DashboardRoutingModule } from './dashboard-routing.module';
import {AirHumidityService} from '../../services/air-humidity.service';
import {AirTemperatureService} from '../../services/air-temperature.service';
import {Co2Service} from '../../services/co2.service';
import {LuminosityService} from '../../services/luminosity.service';
import {PhService} from '../../services/ph.service';
import {PressureService} from '../../services/pressure.service';
import {SoilHumidityService} from '../../services/soil-humidity.service';
import {SoilTemperatureService} from '../../services/soil-temperature.service';

@NgModule({
  imports: [
    FormsModule,
    DashboardRoutingModule,
    ChartsModule,
    BsDropdownModule,
    ButtonsModule.forRoot()
  ],
  declarations: [ DashboardComponent ],
  providers: [
    AirHumidityService,
    AirTemperatureService,
    Co2Service,
    LuminosityService,
    PhService,
    PressureService,
    SoilHumidityService,
    SoilTemperatureService,
  ]
})
export class DashboardModule { }
