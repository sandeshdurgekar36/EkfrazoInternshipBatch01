import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddtestimonialsComponent } from './addtestimonials.component';

describe('AddtestimonialsComponent', () => {
  let component: AddtestimonialsComponent;
  let fixture: ComponentFixture<AddtestimonialsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddtestimonialsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddtestimonialsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
