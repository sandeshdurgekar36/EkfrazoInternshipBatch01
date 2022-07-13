import { TestBed } from '@angular/core/testing';

import { CustaddressService } from './custaddress.service';

describe('CustaddressService', () => {
  let service: CustaddressService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CustaddressService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
