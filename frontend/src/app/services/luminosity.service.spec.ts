import { TestBed } from '@angular/core/testing';

import { LuminosityService } from './luminosity.service';

describe('LuminosityService', () => {
  let service: LuminosityService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LuminosityService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
