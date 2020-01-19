import { TestBed } from '@angular/core/testing';

import { SoilHumidityService } from './soil-humidity.service';

describe('SoilHumidityService', () => {
  let service: SoilHumidityService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SoilHumidityService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
