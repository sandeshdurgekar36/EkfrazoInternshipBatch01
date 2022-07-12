import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StaustComponent } from './staust.component';

describe('StaustComponent', () => {
  let component: StaustComponent;
  let fixture: ComponentFixture<StaustComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StaustComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StaustComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
