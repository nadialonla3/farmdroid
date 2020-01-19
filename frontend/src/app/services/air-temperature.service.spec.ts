import { TestBed } from '@angular/core/testing';

import { AirTemperatureService } from './air-temperature.service';

describe('AirTemperatureService', () => {
  let service: AirTemperatureService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AirTemperatureService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
