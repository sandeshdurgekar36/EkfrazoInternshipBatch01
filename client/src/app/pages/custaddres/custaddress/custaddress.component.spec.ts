import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustaddressComponent } from './custaddress.component';

describe('CustaddressComponent', () => {
  let component: CustaddressComponent;
  let fixture: ComponentFixture<CustaddressComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CustaddressComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CustaddressComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
