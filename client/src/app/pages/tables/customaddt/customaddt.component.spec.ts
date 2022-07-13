import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomaddtComponent } from './customaddt.component';

describe('CustomaddtComponent', () => {
  let component: CustomaddtComponent;
  let fixture: ComponentFixture<CustomaddtComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CustomaddtComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CustomaddtComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
