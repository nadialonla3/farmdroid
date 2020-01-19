import { TestBed } from '@angular/core/testing';

import { PhService } from './ph.service';

describe('PhService', () => {
  let service: PhService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PhService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
