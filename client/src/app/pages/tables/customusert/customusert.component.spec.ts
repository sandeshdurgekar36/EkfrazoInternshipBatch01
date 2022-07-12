import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustomusertComponent } from './customusert.component';

describe('CustomusertComponent', () => {
  let component: CustomusertComponent;
  let fixture: ComponentFixture<CustomusertComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CustomusertComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CustomusertComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
