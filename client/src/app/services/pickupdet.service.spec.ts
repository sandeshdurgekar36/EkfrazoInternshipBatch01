import { TestBed } from '@angular/core/testing';

import { PickupdetService } from './pickupdet.service';

describe('PickupdetService', () => {
  let service: PickupdetService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PickupdetService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
