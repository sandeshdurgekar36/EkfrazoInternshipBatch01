import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CouponstComponent } from './couponst.component';

describe('CouponstComponent', () => {
  let component: CouponstComponent;
  let fixture: ComponentFixture<CouponstComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CouponstComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CouponstComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
