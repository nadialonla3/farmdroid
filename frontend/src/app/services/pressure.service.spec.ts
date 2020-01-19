import { TestBed } from '@angular/core/testing';

import { PressureService } from './pressure.service';

describe('PressureService', () => {
  let service: PressureService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PressureService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
