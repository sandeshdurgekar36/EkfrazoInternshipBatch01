import { TestBed } from '@angular/core/testing';

import { CustomuserService } from './customuser.service';

describe('CustomuserService', () => {
  let service: CustomuserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CustomuserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
