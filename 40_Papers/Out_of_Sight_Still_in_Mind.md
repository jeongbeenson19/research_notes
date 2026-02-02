---
tags:
  - paper
  - AI
  - robotics
  - computer-vision
aliases:
  - Out of Sight, Still in Mind
date: 2024-05-01
---

# Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models

## Abstract

This paper introduces a novel memory-based neural network framework that enables robots to reason and plan about objects that are temporarily unobserved. The model maintains a memory of object poses over several actions, even when objects are occluded from view. This is achieved by taking the current observation, the current action, and a compressed memory of previous observations and actions as input. The paper presents two implementations of this framework: DOOM (Dynamics of Objects in Memory) and LOOM (Latent Objects in Memory), which use point cloud-based and latent space-based memory encoding, respectively.

## Introduction

In real-world scenarios, robots often have to interact with objects that may be temporarily out of sight due to occlusion or limited field of view. To perform complex manipulation tasks, it is crucial for robots to maintain a persistent understanding of the environment, including the state of unobserved objects. This paper addresses the challenge of encoding object-oriented memory into a multi-object manipulation reasoning and planning framework.

## Method

The proposed framework utilizes a memory-based neural network. The core idea is to encode the history of object trajectories from partial-view point clouds, combined with an object discovery and tracking engine. The model learns to predict the future state of the environment, including the poses of occluded objects, based on its memory and the current action.

The two main implementations are:

*   **DOOM (Dynamics of Objects in Memory):** This approach uses a point cloud-based encoding to represent the memory of object states.
*   **LOOM (Latent Objects in Memory):** This approach uses a latent space encoding to represent the memory, which can be more compact and efficient.

Both implementations leverage transformer relational dynamics to model the interactions between objects over time.

## Results

The proposed methods were evaluated in both simulation and real-world experiments. The tasks involved reasoning about occluded objects, handling the appearance of novel objects, and managing object reappearance. The results demonstrate that both DOOM and LOOM perform well and outperform baseline methods that rely on implicit memory.

## Conclusion

This research presents a significant step towards enabling robots to reason and plan in complex environments with occluded objects. The proposed memory-based framework, with its DOOM and LOOM implementations, provides a robust solution for maintaining an internal representation of the world, even when objects are not directly observable. This work has important implications for developing more intelligent and capable robots for a wide range of applications.
