import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllpromocodeComponent } from './allpromocode.component';

describe('AllpromocodeComponent', () => {
  let component: AllpromocodeComponent;
  let fixture: ComponentFixture<AllpromocodeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AllpromocodeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AllpromocodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
