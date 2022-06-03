import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PickupdetComponent } from './pickupdet.component';

describe('PickupdetComponent', () => {
  let component: PickupdetComponent;
  let fixture: ComponentFixture<PickupdetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PickupdetComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PickupdetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
