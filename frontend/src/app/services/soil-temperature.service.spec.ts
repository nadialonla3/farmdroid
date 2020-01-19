import { TestBed } from '@angular/core/testing';

import { SoilTemperatureService } from './soil-temperature.service';

describe('SoilTemperatureService', () => {
  let service: SoilTemperatureService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SoilTemperatureService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
