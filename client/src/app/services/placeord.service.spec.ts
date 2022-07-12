import { TestBed } from '@angular/core/testing';

import { PlaceordService } from './placeord.service';

describe('PlaceordService', () => {
  let service: PlaceordService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PlaceordService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
