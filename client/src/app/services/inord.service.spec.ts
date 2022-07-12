import { TestBed } from '@angular/core/testing';

import { InordService } from './inord.service';

describe('InordService', () => {
  let service: InordService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InordService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
