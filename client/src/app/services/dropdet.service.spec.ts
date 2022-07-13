import { TestBed } from '@angular/core/testing';

import { DropdetService } from './dropdet.service';

describe('DropdetService', () => {
  let service: DropdetService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DropdetService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
