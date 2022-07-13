import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlltestimonialsComponent } from './alltestimonials.component';

describe('AlltestimonialsComponent', () => {
  let component: AlltestimonialsComponent;
  let fixture: ComponentFixture<AlltestimonialsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlltestimonialsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AlltestimonialsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
