import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DrivertComponent } from './drivert.component';

describe('DrivertComponent', () => {
  let component: DrivertComponent;
  let fixture: ComponentFixture<DrivertComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DrivertComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DrivertComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
