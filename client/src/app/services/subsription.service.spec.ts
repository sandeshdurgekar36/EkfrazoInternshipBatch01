import { TestBed } from '@angular/core/testing';

import { SubsriptionService } from './subsription.service';

describe('SubsriptionService', () => {
  let service: SubsriptionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SubsriptionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
