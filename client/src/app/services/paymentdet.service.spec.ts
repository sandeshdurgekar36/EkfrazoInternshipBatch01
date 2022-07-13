import { TestBed } from '@angular/core/testing';

import { PaymentdetService } from './paymentdet.service';

describe('PaymentdetService', () => {
  let service: PaymentdetService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PaymentdetService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
