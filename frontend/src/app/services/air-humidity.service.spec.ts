import { TestBed } from '@angular/core/testing';

import { AirHumidityService } from './air-humidity.service';

describe('AirHumidityService', () => {
  let service: AirHumidityService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AirHumidityService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
