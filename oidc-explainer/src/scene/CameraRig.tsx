import { useThree } from '@react-three/fiber';
import { useEffect } from 'react';
import * as THREE from 'three';

/**
 * A fixed camera.
 *
 * This used to reposition per step, easing toward whichever pair of actors the
 * current hop involved. It read as the whole stage lurching on every step, and
 * moving the frame while also changing what is drawn in it makes both harder to
 * follow. The camera is now set once, wide enough to hold every actor, so the
 * only thing that moves between steps is the packet on the hop itself.
 */
const TARGET = new THREE.Vector3(0, -0.3, 0);

// Half-extents of everything that must stay in shot. Generous on purpose: the
// labels and holding badges are DOM overlays that hang well outside the actor
// boxes, so fitting to the boxes alone clipped them off the edges.
const HALF_WIDTH = 11.0;
const HALF_HEIGHT = 7.0;

export function CameraRig() {
  const { camera, size } = useThree();

  useEffect(() => {
    const cam = camera as THREE.PerspectiveCamera;
    const aspect = size.width / Math.max(size.height, 1);
    const halfFov = ((cam.fov ?? 46) * Math.PI) / 360;

    // Fit both axes and take whichever needs more room. A fixed distance either
    // wasted most of a wide canvas or clipped the stage on a narrow one.
    const forHeight = HALF_HEIGHT / Math.tan(halfFov);
    const forWidth = HALF_WIDTH / (Math.tan(halfFov) * aspect);

    cam.position.set(0, 1.0, Math.max(forHeight, forWidth));
    cam.lookAt(TARGET);
    cam.updateProjectionMatrix();
  }, [camera, size.width, size.height]);

  return null;
}
